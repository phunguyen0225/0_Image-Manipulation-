import numpy as np
import cv2


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """
        
        # add your code here
        shape = image_left.shape

        for row in range(shape[0]):
            for col in range(shape[1]):
                if col in range(column, shape[1]):
                    image_left[row, col] = image_right[row, col]
    
        # Please do not change the structure
        return image_left

    def intensity_scaling(self, input_image, column, alpha, beta):
        """
        Scale your image intensity.

        input_image: the input image
        column: image column at which left section ends
        alpha: left half scaling constant
        beta: right half scaling constant

        return: output_image
        """

        output_image = input_image.copy()

        shape = output_image.shape

        for row in range(shape[0]):
            for col in range(shape[1]):
                if col in range(0, column):
                    output_image[row, col] *= alpha
                else:
                    output_image[row, col] *= beta
        
        # Please do not change the structure
        return output_image

    def centralize_pixel(self, input_image, column):
        """
        Centralize your pixels (do not use np.mean)

        input_image: the input image
        column: image column at which left section ends

        return: output_image
        """

        # add your code here
        output_image = input_image.copy()

        getShape = output_image.shape

        left_average = 0
        left_total = 0

        right_average = 0
        right_total = 0

        for row in range(getShape[0]):
            for col in range(getShape[1]):
                if col in range(0, column):
                    left_average += output_image[row, col]
                    left_total += 1
                else:
                    right_average += output_image[row, col]
                    right_total += 1
        
        left_average /= left_total
        right_average /= right_total 

        left_offset = 128 - left_average
        right_offset = 128 - right_average

        for row in range(getShape[0]):
            for col in range(getShape[1]):
                if col in range(0, column):
                    adjusted = left_offset + output_image[row, col]
                else:
                    adjusted = right_offset + output_image[row, col]

                if adjusted > 255:
                    adjusted = 255
                if adjusted < 0:
                    adjusted = 0
                output_image[row, col] = adjusted

        return output_image
