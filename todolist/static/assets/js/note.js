const noteForm = document.getElementById('noteForm');
const noteInput = document.getElementById('noteInput');
const notesContainer = document.getElementById('notesContainer');

let notes = [];

// Display notes
function displayNotes() {
    notesContainer.innerHTML = '';
    notes.forEach((note, index) => {
        const noteElement = document.createElement('div');
        noteElement.classList.add('note');
        noteElement.innerHTML = `
            <p>${note}</p>
            <button class="delete-btn" onclick="deleteNote(${index})">X</button>
        `;
        notesContainer.appendChild(noteElement);
    });
}

// Add note
function addNote() {
    const noteText = noteInput.value.trim();
    if (noteText !== '') {
        notes.push(noteText);
        noteInput.value = '';
        displayNotes();
    }
}

// Delete note
function deleteNote(index) {
    notes.splice(index, 1);
    displayNotes();
}

// Form submit event
noteForm.addEventListener('submit', function (e) {
    e.preventDefault();
    addNote();
});
