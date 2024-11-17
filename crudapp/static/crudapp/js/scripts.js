// scripts.js
document.addEventListener('DOMContentLoaded', () => {
    const deleteLinks = document.querySelectorAll('a[href*="customer_delete"]');

    deleteLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            if (!confirm('Are you sure you want to delete this customer?')) {
                event.preventDefault();
            }
        });
    });
});
