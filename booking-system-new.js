// ========================================
// BOOKING SYSTEM - UPDATED VERSION
// ========================================

// Variables globales
let selectedTechnician = '';
let selectedService = '';
let selectedServiceDuration = 0;
let selectedDate = '';
let selectedTime = '';
let selectedRemoval = false;
let estimatedDuration = 0;

// Datos de servicios con tiempos base y tiempos de retiro
const serviceData = {
    'Gelish': { duration: 90, removalTime: 30 },
    'Rubber Base': { duration: 120, removalTime: 30 },
    'Acrylic': { duration: 180, removalTime: 60 },
    'Polygel': { duration: 180, removalTime: 60 },
    'Express Pedicure': { duration: 60, removalTime: 0 },
    'Russian Pedicure': { duration: 90, removalTime: 0 },
    'Mystic Pedicure': { duration: 90, removalTime: 0 }
};

// Horarios de las técnicas (desde 9 AM)
const technicianSchedules = {
    'Carolina': {
        'Monday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00'],
        'Tuesday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00'],
        'Wednesday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00'],
        'Thursday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00'],
        'Friday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00'],
        'Saturday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']
    },
    'Monse': {
        'Monday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00'],
        'Tuesday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00'],
        'Wednesday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00'],
        'Thursday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00'],
        'Friday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00'],
        'Saturday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']
    },
    'Diana': {
        'Monday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'],
        'Tuesday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'],
        'Wednesday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'],
        'Thursday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'],
        'Friday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'],
        'Saturday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'],
        'Sunday': ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']
    }
};

// ========================================
// FUNCIONES DEL SISTEMA DE BOOKING
// ========================================

function openBookingModal() {
    document.getElementById('bookingModal').style.display = 'flex';
    document.getElementById('appointmentDate').min = new Date().toISOString().split('T')[0];
    goToStep(1);
}

function closeBookingModal() {
    document.getElementById('bookingModal').style.display = 'none';

    // Reset form
    selectedTechnician = '';
    selectedService = '';
    selectedServiceDuration = 0;
    selectedDate = '';
    selectedTime = '';
    selectedRemoval = false;
    estimatedDuration = 0;

    document.getElementById('clientName').value = '';
    document.getElementById('clientPhone').value = '';
    document.getElementById('specialRequests').value = '';

    // Reset buttons styling
    document.querySelectorAll('.service-btn').forEach(btn => {
        btn.style.background = 'white';
        btn.style.color = 'var(--dark)';
    });

    document.querySelectorAll('.removal-btn').forEach(btn => {
        btn.style.background = 'white';
        btn.style.color = 'var(--dark)';
    });
}

function selectTechnician(tech) {
    selectedTechnician = tech;
    document.getElementById('selectedTechnicianName').textContent = tech;
    goToStep(2);
}

function selectService(service, duration) {
    selectedService = service;
    selectedServiceDuration = duration;

    // Highlight selected service button
    document.querySelectorAll('.service-btn').forEach(btn => {
        btn.style.background = btn.textContent.includes(service) ? 'var(--primary)' : 'white';
        btn.style.color = btn.textContent.includes(service) ? 'white' : 'var(--dark)';
    });

    // Show removal option for manicure services
    if (['Gelish', 'Rubber Base', 'Acrylic', 'Polygel'].includes(service)) {
        document.getElementById('removalOption').style.display = 'block';
    } else {
        document.getElementById('removalOption').style.display = 'none';
        selectedRemoval = false;
    }

    // Calculate and display estimated time
    calculateEstimatedTime();

    document.getElementById('step2NextBtn').disabled = false;
}

function selectRemoval(includeRemoval) {
    selectedRemoval = includeRemoval;

    // Highlight selected removal button
    if (includeRemoval) {
        document.getElementById('yesRemovalBtn').style.background = 'var(--primary)';
        document.getElementById('yesRemovalBtn').style.color = 'white';
        document.getElementById('noRemovalBtn').style.background = 'white';
        document.getElementById('noRemovalBtn').style.color = 'var(--dark)';
    } else {
        document.getElementById('noRemovalBtn').style.background = 'var(--primary)';
        document.getElementById('noRemovalBtn').style.color = 'white';
        document.getElementById('yesRemovalBtn').style.background = 'white';
        document.getElementById('yesRemovalBtn').style.color = 'var(--dark)';
    }

    // Recalculate estimated time
    calculateEstimatedTime();
}

function calculateEstimatedTime() {
    let totalTime = selectedServiceDuration;

    // Add removal time if applicable
    if (selectedRemoval && serviceData[selectedService]) {
        totalTime += serviceData[selectedService].removalTime;
    }

    estimatedDuration = totalTime;

    // Display estimated time
    const hours = Math.floor(totalTime / 60);
    const minutes = totalTime % 60;
    let timeString = '';

    if (hours > 0) {
        timeString += hours + ' hour' + (hours > 1 ? 's' : '') + ' ';
    }
    timeString += minutes + ' minute' + (minutes !== 1 ? 's' : '');

    document.getElementById('estimatedTime').textContent = timeString;
    document.getElementById('timeEstimate').style.display = 'block';
}

function goToStep(step) {
    document.querySelectorAll('.booking-step').forEach(s => s.style.display = 'none');
    document.getElementById('step' + step).style.display = 'block';
}

function updateTimeSlots() {
    const dateInput = document.getElementById('appointmentDate');
    const timeSlotsContainer = document.getElementById('timeSlots');
    const dayName = new Date(dateInput.value + 'T00:00:00').toLocaleDateString('en-US', { weekday: 'long' });

    const slots = technicianSchedules[selectedTechnician]?.[dayName] || [];

    timeSlotsContainer.innerHTML = '';
    slots.forEach(time => {
        const btn = document.createElement('button');
        btn.textContent = time;
        btn.onclick = () => selectTime(time);
        btn.style.cssText = 'padding: 10px; border: 2px solid var(--primary); border-radius: 8px; background: white; cursor: pointer; transition: all 0.3s ease;';
        timeSlotsContainer.appendChild(btn);
    });

    document.getElementById('step3NextBtn').disabled = true;
}

function selectTime(time) {
    selectedTime = time;

    // Calculate end time
    const [hours, minutes] = time.split(':').map(Number);
    const startDate = new Date(selectedDate + 'T' + time + ':00');
    const endDate = new Date(startDate.getTime() + estimatedDuration * 60000);

    document.querySelectorAll('#timeSlots button').forEach(btn => {
        btn.style.background = btn.textContent === time ? 'var(--primary)' : 'white';
        btn.style.color = btn.textContent === time ? 'white' : 'var(--dark)';
    });

    document.getElementById('step3NextBtn').disabled = false;

    // Update confirmation details
    updateConfirmationDetails();
}

function updateConfirmationDetails() {
    document.getElementById('confirmTechnician').textContent = selectedTechnician;
    document.getElementById('confirmService').textContent = selectedService;
    document.getElementById('confirmTimeEstimate').textContent = document.getElementById('estimatedTime').textContent;
}

document.getElementById('appointmentDate').addEventListener('change', function() {
    selectedDate = this.value;
    updateTimeSlots();
});

function confirmBooking() {
    const name = document.getElementById('clientName').value;
    const phone = document.getElementById('clientPhone').value;
    const specialRequests = document.getElementById('specialRequests').value;

    if (!name || !phone) {
        alert('Please fill in your name and phone number');
        return;
    }

    // Calculate end time for display
    const [hours, minutes] = selectedTime.split(':').map(Number);
    const startDate = new Date(selectedDate + 'T' + selectedTime + ':00');
    const endDate = new Date(startDate.getTime() + estimatedDuration * 60000);
    const endTime = endDate.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });

    const formattedDate = new Date(selectedDate + 'T00:00:00').toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });

    // Send WhatsApp confirmation with all details
    const removalText = selectedRemoval ? '✅ With Removal' : '❌ No Removal';
    const whatsappMsg = `✨ NEW BOOKING REQUEST ✨%0A%0A👤 Client: ${name}%0A📱 Phone: ${phone}%0A%0A📅 APPOINTMENT DETAILS:%0A👩‍🎨 Technician: ${selectedTechnician}%0A💅 Service: ${selectedService}%0A📅 Date: ${formattedDate}%0A⏰ Time: ${selectedTime} - ${endTime}%0A⏱️ Duration: ${document.getElementById('estimatedTime').textContent}%0A💅 Removal: ${removalText}%0A%0A${specialRequests ? '📝 Notes: ' + specialRequests : ''}`;

    window.open(`https://wa.me/529843108186?text=${whatsappMsg}`, '_blank');

    alert('✅ Booking request sent! We will confirm your appointment shortly via WhatsApp.');
    closeBookingModal();
}
