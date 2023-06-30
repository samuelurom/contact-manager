// Get the delete buttons from DOM
const deleteBtn = document.getElementById('delete');

if (deleteBtn) {
  deleteBtn.addEventListener('click', (event) => {
    if (!confirm('Are you sure you want to delete this contact?')) {
      event.preventDefault();
    }
  })
}