function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function() {
        var preview = document.getElementById('preview-image');
        preview.src = reader.result;
    }
    reader.readAsDataURL(event.target.files[0]);
}
