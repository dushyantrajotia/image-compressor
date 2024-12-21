document.getElementById('quality-slider').addEventListener('input', function () {
    const qualityValue = document.getElementById('quality-value');
    qualityValue.textContent = `${this.value}%`;
});

document.getElementById('image-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const resultDiv = document.getElementById('result');

    resultDiv.textContent = 'Compressing... Please wait.';

    fetch('/', {
        method: 'POST',
        body: formData,
    })
        .then((response) => response.blob())
        .then((blob) => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'compressed_image.jpg';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            resultDiv.textContent = 'Image compressed successfully!';
        })
        .catch((error) => {
            resultDiv.textContent = 'An error occurred while compressing the image.';
            console.error('Error:', error);
        });
});
