function [movingReg,Rreg,tform] = imreg_new3(varargin)
        %IMREGISTER Register two 2-D or 3-D images using intensity metric optimization.
        %
        %
        
        tform = imregtform(varargin{:});
        
        % Rely on imregtform to input parse and validate. If we were passed
        % spatially referenced input, use spatial referencing during resampling.
        % Otherwise, just use identity referencing objects for the fixed and
        % moving images.
        spatiallyReferencedInput = isa(varargin{2},'imref2d') && isa(varargin{4},'imref2d');
        if spatiallyReferencedInput
            moving  = varargin{1};
            Rmoving = varargin{2};
            Rfixed  = varargin{4};
        else
            moving = varargin{1};
            fixed = varargin{2};
            if (tform.Dimensionality == 2)
                Rmoving = imref2d(size(moving));
                Rfixed = imref2d(size(fixed));
            else
                Rmoving = imref3d(size(moving));
                Rfixed = imref3d(size(fixed));
            end
        end
        
        % Transform the moving image using the transform estimate from imregtform.
        % Use the 'OutputView' option to preserve the world limits and the
        % resolution of the fixed image when resampling the moving image.
        [movingReg,Rreg] = imwarp(moving,Rmoving,tform,'OutputView',Rfixed);
        
        
    end

