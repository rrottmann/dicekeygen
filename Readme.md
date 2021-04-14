# dicekeygen
In case you did not already receive your physical DiceKeys from https://dicekeys.com/ but still want to use the IOS/Android app,
you can use this small Python script to throw some dices that you can manually add to the app.

## Example
```
G6U S4U Y2D U4U T3U
D3L Z4D L2L A3L F6R
E2R O6L N2D X6D K5U
W5R V5R H4U B6U P5R
J6U I5L C3L R6D M4U
```
`G6`: Regular dice face, `U` is the direction and one of `U`, `D`, `L`, `R`.
Together this creates 124,127,134,662,179,891,202,329,100,571,859,806,502,566,406,865,813,504,000,000 possible keys!

Of course the physical dices are absolutely random throws. This script uses the `secrets` library to use cryptographical
grade randomness.