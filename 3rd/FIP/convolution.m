
A = imread('ki.jpg');
B = rgb2gray(A);

m1 = (1/9)+ones(3,3);
m2 = (1/25)+ones(5,5);

h1 = conv2(B, m1, 'same');
h2 = conv2(B,  m2, 'same');

subplot(2, 2, 1), imshow(B), title('orginal image');
subplot(2, 2, 2), imshow(uint8(h1)), title('conv 3');
subplot(2, 2, 3), imshow(uint8(h2)), title('conv 5');


