# splatify
12/11/21: I need a way to create animations for converting a starting shape (roughly circular) into a "splatted" shape. I have mathematical definitions of the starting and ending shape outlines in polar coordinates and render them as SVG. I am going to try to use optimal transport to create an automated mapping between the two to create animations by converting the radius vs. theta disributions. I want to add the ability to add noise to this transition (i.e. via damping parameter) so that the "splat" effect has some extra fun factor. I would like to write this in a way that allows others to use this tool if they wish.


https://user-images.githubusercontent.com/95984476/145927422-e85d1af1-62b7-4267-a964-5afdfc7cc99e.mp4

