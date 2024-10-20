const btn = document.querySelector('.btn');
        const pixelGrid = document.querySelector('.pixel-grid');

        // Create 50 pixels
        for (let i = 0; i < 50; i++) {
            const pixel = document.createElement('div');
            pixel.classList.add('pixel');
            pixelGrid.appendChild(pixel);
        }

        // Add random delay to each pixel's animation
        document.querySelectorAll('.pixel').forEach(pixel => {
            pixel.style.animationDelay = `${Math.random() * 2}s`;
        });

        function openQRCode() {
            var image = document.querySelector('.qr-result img');
            var w = window.open("");
            w.document.write(image.outerHTML);
        }