a=imread('office_2.jpg');
b=rgb2gray(a);
c=imnoise(b,'salt & pepper',0.05);
resimg=medfilt2(c);
subplot(2,2,1),imshow(a),title('original image');
subplot(2,2,2),imshow(c),title('salt&pepper');
subplot(2,2,3),imshow(resimg),title('restored(median)');
PSNR_org=psnr(b,c)
psnr_res=psnr(resimg,b)
mse_org=immse(b,c)
mse_res=immse(resimg,b)