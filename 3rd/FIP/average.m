a=imread('office_1.jpg');
b=rgb2gray(a);
c=imnoise(b,'salt & pepper',0.05);
C=fspecial('average',[9,9]);            %exact 9x9 average filter 
d=imfilter(b,C);
subplot(2,2,1),imshow(a),title('original image');
subplot(2,2,2),imshow(c),title('salt&pepper');
subplot(2,2,3),imshow(d),title('restored image');
PSNR_org=psnr(b,c)
psnr_res=psnr(d,b)
mse_org=immse(b,c)
mse_res=immse(d,b)