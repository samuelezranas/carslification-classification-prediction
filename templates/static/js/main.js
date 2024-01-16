// Fungsi untuk menampilkan atau menyembunyikan tombol Submit dan Cancel Input
document.getElementById('file-input').addEventListener('change', function() {
    var submitBtn = document.getElementById('submitBtn');
    var cancelBtn = document.getElementById('cancelBtn');

    if (this.value) {
        submitBtn.style.display = 'inline-block';
        cancelBtn.style.display = 'inline-block';
    } else {
        submitBtn.style.display = 'none';
        cancelBtn.style.display = 'none';
    }
});

// Fungsi untuk menghapus file yang telah dipilih dan menyembunyikan tombol Submit dan Cancel Input
document.getElementById('cancelBtn').addEventListener('click', function() {
    var fileInput = document.getElementById('file-input');
    fileInput.value = ''; // Menghapus nilai file input
    document.getElementById('submitBtn').style.display = 'none';
    this.style.display = 'none';
});

document.getElementById("submitBtn").addEventListener("click", function(event) {
    // Prevent the default form submission
    event.preventDefault();
    
    // Code to show the result section
    var resultSection = document.getElementById("result-section");
    resultSection.style.display = "block";

    // Hide submitBtn and cancelBtn
    var submitBtn = document.getElementById('submitBtn');
    var cancelBtn = document.getElementById('cancelBtn');
    submitBtn.style.display = 'none';
    cancelBtn.style.display = 'none';

    setTimeout(function() {
        resultSection.style.display = "none";
        submitBtn.style.display = 'none';
        cancelBtn.style.display = 'none';
    }, 10000);
});