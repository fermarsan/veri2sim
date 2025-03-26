# Verilog to SimulIDE blocks converter

This is a simple _*Verilog*_ to [_*SimulIDE*_](https://simulide.com/p/) block converter written in _Python_ using the _PLY_ module.

## Usage

```bash
python veri2sim.py --compile verilog_file.v
```

The last command generates the files:
```
verilog_file.package
verilog_file.mcu
verilog_file.as
```

These files are necessary to [implement a block on SimulIDE by a script](https://simulide.com/p/scripted/).

## Prerequisites
Python 3.6 or higher with the following modules:
- `ply`
- `lxml`

## Limitations
For now `veri2sim` only supports simple examples including `wire` declarations and the `assign` command

## Simple NOT gate example

This verilog file `not.v`:

```verilog
module not (input a, output b);
    wire w;
    assign w = ~a;
    assign b = w;
endmodule
```

generates:

- `not.package`

```xml
<!DOCTYPE SimulIDE>

<!-- This file was generated by veri2sim -->

<packageB name="Package" width="8" height="2" background="" type="None">
  <pin type="" xpos="-8" ypos="8" angle="180" length="8" space="0" id="a" label="a"/>
  <pin type="" xpos="72" ypos="8" angle="0" length="8" space="0" id="b" label="b"/>
</packageB>
```

- `not.mcu`
  
```xml
<!DOCTYPE SimulIDE>

<!-- This file was generated by veri2sim -->

<iou name="not" core="scripted" script="not.as">
  <ioport name="SinglePinsPort" pins="a,b"/>
</iou>
```

- and `not.as` (AngelScript)

```cpp
// This file was generated by veri2sim

IoPin@ aPin = component.getPin("a");
IoPin@ bPin = component.getPin("b");

// ___global_definitions___
bool w = false;

void setup()
{
	print("not setup()");
}

void reset()
{
	print("not reset()");

	aPin.setPinMode(1); // Input
	aPin.changeCallBack(element, true);
	bPin.setPinMode(3); // Output
	bPin.setOutState(false);
}

void voltChanged()
{
	// ___implementation___
	w = !aPin.getInpState();
	bPin.setOutState(w);
}
```

### On SimulIDE

![](/assets/simulation.png)


