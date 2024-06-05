a=imread('flower.jpg');
b=rgb2gray(a);
c=histeq(b);
subplot(2,2,1),imshow(a),title('original');
subplot(2,2,2),imhist(b),title('hist');
subplot(2,2,3),imshow(c),title('c');
subplot(2,2,4),imhist(c),title('histeq');