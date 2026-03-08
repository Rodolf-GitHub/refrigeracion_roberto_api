document.addEventListener('DOMContentLoaded', function () {
    function attachPreview(input) {
        if (input.dataset.previewBound) return;
        input.dataset.previewBound = '1';

        input.addEventListener('change', function () {
            var file = this.files && this.files[0];
            var row = this.closest('tr') || this.closest('.inline-related');
            if (!row) return;
            var img = row.querySelector('.preview-img');
            var placeholder = row.querySelector('.preview-placeholder');

            if (file && file.type.startsWith('image/')) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    if (img) { img.src = e.target.result; img.style.display = 'inline-block'; }
                    if (placeholder) placeholder.style.display = 'none';
                };
                reader.readAsDataURL(file);
            } else {
                if (img) { img.src = ''; img.style.display = 'none'; }
                if (placeholder) placeholder.style.display = 'inline';
            }
        });
    }

    // Inputs existentes
    document.querySelectorAll('#imagenes-group input[type="file"]').forEach(attachPreview);

    // Nuevos inlines: observar cambios en el DOM
    var group = document.getElementById('imagenes-group');
    if (group) {
        new MutationObserver(function () {
            group.querySelectorAll('input[type="file"]').forEach(attachPreview);
        }).observe(group, { childList: true, subtree: true });
    }
});
