from cv2 import cv2, countNonZero, cvtColor
import numpy as np

im1 = cv2.imread('images/blank_scan.png')
im2 = cv2.imread('images/base_scan.png')

warp_mode = cv2.MOTION_AFFINE
warp_matrix = np.eye(2, 3, dtype=np.float32)

# Specify the number of iterations.
number_of_iterations = 100

# Specify the threshold of the increment in the correlation
# coefficient between two iterations
termination_eps = 1e-7

criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
            number_of_iterations, termination_eps)

# Run the ECC algorithm. The results are stored in warp_matrix.
(cc, warp_matrix) = cv2.findTransformECC(im1, im2, warp_matrix,
                                         warp_mode, criteria)


# Get the target size from the desired image
target_shape = im1.shape

aligned_image = cv2.warpAffine(
                          im2,
                          warp_matrix,
                          (target_shape[1], target_shape[0]),
                          flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP,
                          borderMode=cv2.BORDER_CONSTANT,
                          borderValue=0)

cv2.imwrite('images/aligned.png', aligned_image)