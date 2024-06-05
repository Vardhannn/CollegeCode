b=imread('football.jpg');

subplot(2,2,1),imshow(b),title('original Image');
c=imnoise(b,'salt & pepper',0.05);
d=imnoise(b,'gaussian',0.07);
e=imnoise(b,'poisson');
subplot(2,2,2),imshow(c),title('salt and pepper noise');
subplot(2,2,3),imshow(d),title('gaussian');
subplot(2,2,4),imshow(e),title('poisson');
peaksnr=psnr(c,b);
d=immse(c,b);
fprintf('\n peak snr value is %0.4f',peaksnr);
fprintf('\n The mean-squared error is %0.4f\n',d);