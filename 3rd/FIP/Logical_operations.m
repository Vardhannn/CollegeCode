A=imread('fox.jpg');
B=imread('fox.png');
c=imresize(B,[183,275]);
d=bitand(A,c);
e=bitor(A,c);
f=bitxor(A,c);
g=imcomplement(A);
subplot(3,2,1),imshow(A),title('Image 1');
subplot(3,2,2),imshow(c),title('image 2');
subplot(3,2,3),imshow(g),title('COMPLEMENT');
subplot(3,2,4),imshow(d),title('AND');
subplot(3,2,5),imshow(e),title('OR');
subplot(3,2,6),imshow(f),title('XOR');



