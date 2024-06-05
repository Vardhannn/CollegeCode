original_image = imread('gantrycrane.png');

if size(original_image, 3) == 3
    gray_image = rgb2gray(original_image);
else
    gray_image = original_image;
end


dct_image = dct2(double(gray_image));

% Step 4: Define compression ratio (e.g., 0.1 means retain top 10% of coefficients)
compression_ratio = 0.1;

% Step 5: Thresholding to retain only top coefficients
dct_image_compressed = dct_image;
num_coeffs = numel(dct_image);
num_coeffs_retained = ceil(compression_ratio * num_coeffs);
[sorted_coeffs, sorted_indices] = sort(abs(dct_image(:)), 'descend');
threshold = sorted_coeffs(num_coeffs_retained);
dct_image_compressed(abs(dct_image) < threshold) = 0;

% Step 6: Perform inverse DCT
reconstructed_image = idct2(dct_image_compressed);

% Step 7: Display original and reconstructed images
figure;
subplot(1, 2, 1);
imshow(gray_image);
title('Original Image');
subplot(1, 2, 2);
imshow(uint8(reconstructed_image));
title('Reconstructed Image');

% Step 8: Calculate compression ratio and image quality
compression_ratio_actual = nnz(dct_image_compressed) / num_coeffs;
mse = sum(sum((double(gray_image) - reconstructed_image).^2)) / numel(gray_image);
psnr = 10 * log10(255^2 / mse);

fprintf('Compression Ratio (Actual): %.2f\n', compression_ratio_actual);
fprintf('MSE: %.2f\n', mse);
fprintf('PSNR: %.2f dB\n', psnr);

% Step 9: Save the compressed image
imwrite(uint8(reconstructed_image), 'compressed_image.jpg');