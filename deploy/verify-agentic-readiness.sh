#!/usr/bin/env bash
# Verifies the 5 "Is Agentic" audit fixes against the live site.
# Usage: ./verify-agentic-readiness.sh [https://mysticnailsart.com]
set -uo pipefail
BASE="${1:-https://mysticnailsart.com}"
PASS=0
FAIL=0

check() {
  local desc="$1" got="$2" want="$3"
  if [ "$got" = "$want" ]; then
    echo "PASS: $desc"
    PASS=$((PASS+1))
  else
    echo "FAIL: $desc (got: $got, want: $want)"
    FAIL=$((FAIL+1))
  fi
}

echo "== 1. Content without JavaScript =="
TEXT_LEN=$(curl -s "$BASE/" | python3 -c "
import sys, re
c = sys.stdin.read()
idx = c.find('<script type=\"__bundler/template\">')
pre = c[:idx] if idx != -1 else c
no_script = re.sub(r'<script\b[^>]*>.*?</script>', '', pre, flags=re.S)
no_style = re.sub(r'<style\b[^>]*>.*?</style>', '', no_script, flags=re.S)
text = re.sub(r'<[^>]+>', ' ', no_style)
print(len(re.sub(r'\s+', ' ', text).strip()))
")
if [ "$TEXT_LEN" -ge 500 ]; then echo "PASS: raw text length $TEXT_LEN >= 500"; PASS=$((PASS+1)); else echo "FAIL: raw text length $TEXT_LEN < 500"; FAIL=$((FAIL+1)); fi
H1=$(curl -s "$BASE/" | grep -oE '<h1[^>]*>[^<]*' | head -1)
if [ -n "$H1" ]; then echo "PASS: H1 present in raw HTML"; PASS=$((PASS+1)); else echo "FAIL: no H1 in raw HTML"; FAIL=$((FAIL+1)); fi

echo ""
echo "== 2. Agent-friendly 404s =="
CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE/this-path-does-not-exist-xyz")
check "404 status code" "$CODE" "404"
BODY_HAS_LINKS=$(curl -s "$BASE/this-path-does-not-exist-xyz" | grep -c "sitemap.xml\|llms.txt")
if [ "$BODY_HAS_LINKS" -gt 0 ]; then echo "PASS: 404 body links to sitemap/llms.txt"; PASS=$((PASS+1)); else echo "FAIL: 404 body missing recovery links"; FAIL=$((FAIL+1)); fi

echo ""
echo "== 3. Markdown content negotiation =="
CT=$(curl -s -H "Accept: text/markdown" -D - -o /dev/null "$BASE/" | grep -i "^content-type" | tr -d '\r')
check "Content-Type on markdown request" "$CT" "Content-Type: text/markdown; charset=utf-8"
VARY_COUNT=$(curl -s -H "Accept: text/markdown" -D - -o /dev/null "$BASE/" | grep -ic "^vary")
check "single Vary header" "$VARY_COUNT" "1"
VARY_VAL=$(curl -s -D - -o /dev/null "$BASE/" | grep -i "^vary" | tr -d '\r')
case "$VARY_VAL" in
  *Accept*) echo "PASS: Vary includes Accept"; PASS=$((PASS+1));;
  *) echo "FAIL: Vary missing Accept ($VARY_VAL)"; FAIL=$((FAIL+1));;
esac
MD_404_CODE=$(curl -s -H "Accept: text/markdown" -o /dev/null -w "%{http_code}" "$BASE/nonexistent-xyz")
check "404 + markdown still 404" "$MD_404_CODE" "404"

echo ""
echo "== 5. JSON-LD structured data =="
JSONLD_COUNT=$(curl -s "$BASE/" | python3 -c "
import sys, re
c = sys.stdin.read()
idx = c.find('<script type=\"__bundler/template\">')
pre = c[:idx] if idx != -1 else c
print(pre.count('application/ld+json'))
")
if [ "$JSONLD_COUNT" -ge 1 ]; then echo "PASS: $JSONLD_COUNT JSON-LD block(s) in raw HTML"; PASS=$((PASS+1)); else echo "FAIL: no JSON-LD in raw HTML"; FAIL=$((FAIL+1)); fi

echo ""
echo "== 4. Brand discoverability (code-controllable checks only) =="
REDIRECT=$(curl -s -o /dev/null -w "%{http_code}" "https://www.mysticnailsart.com/")
check "www redirects (single hop)" "$REDIRECT" "301"
CANONICAL=$(curl -s "$BASE/" | grep -c 'rel="canonical" href="https://mysticnailsart.com/"')
if [ "$CANONICAL" -gt 0 ]; then echo "PASS: canonical tag present"; PASS=$((PASS+1)); else echo "FAIL: canonical tag missing"; FAIL=$((FAIL+1)); fi

echo ""
echo "===================="
echo "PASS: $PASS  FAIL: $FAIL"
[ "$FAIL" -eq 0 ]
