D1 = 'PathofDataPreprocessImages;
S1 = dir(fullfile(D1,'*.bmp')); % pattern to match filenames.  
i=1;
for k = 1:numel(S1)   %number of array elements.
    F = fullfile(D1,S1(k).name);
    image = imread(F); 
    % Görüntü RGB ise;
    if size(image,3)==3
%         image= rgb2gray(image);
        redChannel = image(:, :, 1);
        greenChannel = image(:, :, 2);
        blueChannel = image(:, :, 3);
        sdR = std2(redChannel);
        sdG = std2(greenChannel);
        sdB = std2(blueChannel);

        avgRGB = mean(reshape(image, [], 3), 1);

        hsvImage=rgb2hsv(image);
        hChannel = hsvImage(:,:,1); %H Component
        sChannel = hsvImage(:,:,2); %S Component
        vChannel = hsvImage(:,:,3); %I Component
        sdH = std2(hChannel);
        sdS = std2(sChannel);
        sdV = std2(vChannel);

        avgHSV = mean(reshape(hsvImage, [], 3), 1);

        cieImage = rgb2lab(image); %???????????????????????????
        cChannel = cieImage(:,:,1); 
        iChannel = cieImage(:,:,2); 
        eChannel = cieImage(:,:,3); 
        sdC = std2(cChannel);
        sdI = std2(iChannel);
        sdE = std2(eChannel);
        avgCIE = mean(reshape(cieImage, [], 3), 1);

        v1=[avgRGB avgHSV avgCIE sdR sdG sdB sdH sdS sdV sdC sdI sdE];
%     image = cat(3, image, image, image);  %conversion RGB to GScale
%------------------------------------------FS-GLCM--------------------
        gImage = rgb2gray(image);
        gImage=double(gImage);

    % suppose name of the matrix is 'm'
        [a,b]=size(gImage);
        s=sum(gImage);         % sum of all columns
        total=sum(s);     % total sum
        avg=total/(a*b);   

    %meanValue=mean2(gImage);
    %n=std2(gImage);

        ust=0;  skust=0;  enj=0; ent=0;
        for row=1:a
            for col=1:b
              ust=ust+((gImage(row,col)-avg)^2);
              skust=skust+((gImage(row,col)-avg)^3);
              ent= ent + (gImage(row,col)*(-(log2(gImage(row,col)))));
              enj= enj + (gImage(row,col))^2;
            end
        end

        mstd=(ust/(a*b))^0.5;
        mvar=mstd^2;
        msk=skust/(a*b*mstd*mstd);
        ment=ent/(a*b);
        menj=enj/(a*b);

%GLCM---------------------------------
        gImage = rgb2gray(image);
        glcms = graycomatrix(gImage);
        statsg = graycoprops(glcms);

        v2=[avg mstd mvar msk ment menj];

        feature_vektor=[v1 v2 statsg.Contrast statsg.Correlation statsg.Energy statsg.Homogeneity];
    
    A(i,:)=feature_vektor;
    
    % Make the caption the block number.
    % Increment the subplot to the next location.
    i=i+1;
    end
end
