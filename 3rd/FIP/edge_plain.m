a=imread('moon.tif');
b=(a);
c=edge(b,'roberts');
d=edge(b,'sobel');
e=edge(b,'prewitt');
f=edge(b,'canny');
subplot(2,2,1),imshow(b),title('Original Image')
subplot(2,2,2),imshow(c),title('Robert')
subplot(2,2,3),imshow(d),title('Sobel')
subplot(2,2,4),imshow(e),title('Canny')
