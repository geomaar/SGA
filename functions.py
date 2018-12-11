import numpy as np
import math

def st_coord_line(trd,plg,sttype):
    """ 
    StCoordLine computes the coordinates of a line 
    in an equal angle or equal area stereonet of unit radius
    
    Args:
        trd: trend of line
        plg: plunge of line
        sttype: An integer indicating the type of stereonet. 0 for equal angle
            and 1 for equal area
            
    Returns:
        xp and xy: Coordinates of the line in the stereonet plot
    
    
    NOTE: trend and plunge should be entered in radians
    
    StCoordLine uses function ZeroTwoPi

    Python script written by Nestor Cardozo for the book Structural 
    Geology Algorithms by Allmendinger, Cardozo, & Fisher, 2011. If you use
    this script, please cite this as "Cardozo in Allmendinger et al. (2011)"
    """
    
    # Take care of negative plunges
    if plg < 0.0:
        trd = functions.zero_two_pi(trd+math.pi)
        plg = -plg


    # Some constants
    piS4 = math.pi/4.0
    s2 = math.sqrt(2.0)
    plgS2 = plg/2.0

    # Equal angle stereonet: From Equation 1.5 above
    # Also see Pollard and Fletcher (2005), eq.2.72
    if sttype == 0:
        xp = math.tan(piS4 - plgS2)*math.sin(trd)
        yp = math.tan(piS4 - plgS2)*math.cos(trd)
        
    # Equal area stereonet: From Equation 1.6 above
    # Also see Pollard and Fletcher (2005), eq.2.90
    elif sttype == 1:
        xp = s2*math.sin(piS4 - plgS2)*math.sin(trd)
        yp = s2*math.sin(piS4 - plgS2)*math.cos(trd)
    return xp
    return yp

def zero_two_pi(a):
    """
    ZeroTwoPi constrains azimuth to lie between 0 and 2*pi radians 
    
    Args:
        a: input azimuth (which may not be between 0 to 2*pi)
        
    Returns:   
        b: output azimuth (from 0 to 2*pi)

    NOTE: Azimuths a and b are input/output in radians 

    Python script written by Nestor Cardozo for the book Structural 
    Geology Algorithms by Allmendinger, Cardozo, & Fisher, 2011. If you use
    this script, please cite this as "Cardozo in Allmendinger et al. (2011)"
    """
    b=a
    twopi = 2.0*math.pi
    if b < 0.0:
        b = b + twopi
    elif b >= twopi:
        b = b - twopi
    
    return b