# splatify
This function does the following:
1) Generates an initial "blob" shape based on a preset number of interpolated radii, sampled from a normal distribution with mean and st. deviation of m1, s1.
2) Generates a final "blob" shape based on aforementioned number of interpolated radii, sampled from a normal distribution with mean and st. deviation of m2, s2.
3) Uses an underdamped sine wave with assigned damping ratio to interpolate between initial and final states with a small overshoot, simulating a "splat".
 
![image](https://user-images.githubusercontent.com/95984476/145927747-0d075ac0-961b-4c9c-841d-864036969b63.png)

![image](https://user-images.githubusercontent.com/95984476/145927998-a99e1f1d-c984-4403-b43b-2fb5a8c33fb1.png)

4) Saves images together in a directory of your choosing.


https://user-images.githubusercontent.com/95984476/145927422-e85d1af1-62b7-4267-a964-5afdfc7cc99e.mp4

