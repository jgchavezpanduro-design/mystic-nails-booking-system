import os

files = [f for f in os.listdir('assets/imagenes/watermarked') if f.endswith('.jpeg')]
chunks = [files[i:i + 4] for i in range(0, len(files), 4)]

html = '                <div class="hero-image">\n'
html += '                    <div class="hero-carousel" style="width: 100%; aspect-ratio: 1; position: relative; overflow: hidden; border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.15);">\n'
html += '                        <div class="hero-carousel-track" id="heroCarouselTrack" style="display: flex; transition: transform 0.6s ease-in-out; width: 400%; height: 100%;">\n'

for chunk in chunks:
    html += '                            <div class="hero-slide" style="width: 25%; height: 100%; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 4px; padding: 4px; background: var(--light);">\n'
    for f in chunk:
        html += f'                                <img src="assets/imagenes/watermarked/{f}" alt="Nail Art Design" class="lightbox-trigger" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; cursor: pointer; transition: transform 0.3s;" onmouseover="this.style.transform=\'scale(1.02)\'" onmouseout="this.style.transform=\'scale(1)\'">\n'
    html += '                            </div>\n'

html += '                        </div>\n'
html += '                    </div>\n'
html += '                </div>'

with open('hero_gallery.html', 'w') as f:
    f.write(html)
