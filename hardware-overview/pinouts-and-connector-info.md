# Pinouts and Connector info

## HoverGames Interposer Board \(HGI\)

The HoverGames Interposer Board has a large amount of connectors and I/O for you to connect your devices, sensors, switches, LEDs, and more. This section will give you an overview of the connector pinouts on the HGI. The picture below has a few silkscreen labels for pinouts on each connector, but some connectors have multiplexers to make them more flexible.

![Overview of the HoverGames Interposer Board](../.gitbook/assets/image%20%2821%29.png)

## UART2

UART2 is used for the serial monitor, and should not be used for anything other than the serial monitor. It should not be altered.

![](../.gitbook/assets/image%20%2827%29.png)

## UART3

UART3 will mainly be used for serial communication to the FMU in HoverGames, but it can be used as an SPI port if you're not using it for the drone.

![](../.gitbook/assets/image%20%2824%29.png)

## UART4/I2C/GPIO

The bottom 9 pin JST-GH connector in the image of the HGI is used for UART4/I2C/GPIO. The UART4 pins do not have flow control on this connector. There is no multiplexing on this connector as well. The pinout is below.

![](../.gitbook/assets/image%20%2822%29.png)

### Linux GPIO Pin IDs

| GPIO Pin \(JST-GH Pin\) | Linux GPIO ID |
| :--- | :--- |
| GPIO1\_IO10 \(6\) | 10 |
| GPIO1\_IO12 \(7\) | 12 |
| GPIO1\_IO14 \(8\) | 14 |

## SPI/GPIO

The SPI/GPIO port has a full pinout for SPI as well as 3 GPIO pins. The SPI pins can be muxed to a full UART 4 port with flow control. The pinout is below.

![](../.gitbook/assets/image%20%2825%29.png)

### Linux GPIO Pin IDs

| GPIO Pin \(JST-GH Pin\) | Linux GPIO ID |
| :--- | :--- |
| GPIO1\_IO11 \(6\) | 11 |
| GPIO1\_IO13 \(7\) | 13 |
| GPIO1\_IO15 \(8\) | 15 |

## GPIO Headers

The GPIO header pads on the HGI are not labeled correctly with the silkscreen. The layout is shown below with TP labels and schematics.

![GPIO Pin Labels](../.gitbook/assets/image%20%2823%29.png)

![GPIO pinout for labels](../.gitbook/assets/image%20%2826%29.png)

