import launchpad_py as launchpad
import random

if launchpad.LaunchpadMiniMk3().Check(1):
    lp = launchpad.LaunchpadMiniMk3()
    if lp.Open(1, "minimk3"):
        print("Connected to Launchpad Mini Mk3.\n")
    else:
        print("Did not find any Launchpad Mini Mk3...\n")
        exit(0)

lp.Reset()  # turn all LEDs off
LEDcodes = []
x = 11
while x < 100:
    LEDcodes.append(x)
    x += 1
    if not x % 10:
        x += 1

while 1:
    lp.LedCtrlRawByCode(random.choice(LEDcodes), random.randint(0, 127))

lp.Close()  # close the Launchpad

###############################################################################
# Open( [name], [number], [template (*1*)] )
# Close()
# Reset()
# ListAll( [searchString] )
# EventRaw()
# LedSetMode( mode )
# LedGetColorByName( name )
# LedCtrlRaw( number, red, green, [blue] )
# LedCtrlRawByCode( number, [colorcode] )
# LedCtrlPulseByCode( number, colorcode )
# LedCtrlPulseXYByCode( x, y, colorcode )
# LedCtrlFlashByCode( number, colorcode )
# LedCtrlFlashXYByCode( x, y, colorcode )
# LedCtrlBpm( bpm ) # set flashing/pulsing rate
# LedCtrlXY( x, y, red, green, [blue] )
# LedCtrlXYByCode( x, y, colorcode )
# LedCtrlXYByRGB( x, y, colorlist )
# LedCtrlChar( char, red, green, [blue], [offsx], [offsy] )
# LedCtrlString( string, red, green, blue, -1, waitms=25) # Display text
# LedAllOn( [colorcode] )
# ButtonStateRaw( [returnPressure] )
# ButtonStateXY( [mode], [returnPressure] )
# ButtonFlush() # Clear button history
###############################################################################
