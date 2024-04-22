using System.IO.Ports;
using Modbus.Device;
namespace Port_Open
{
 class Program
{
 static void Main(string[] args)
 {
 SerialPort _port;
 ModbusSerialMaster _master;
 string portName = "/dev/ttyUSB0"; // Serial Port 지정
 _port = new SerialPort(portName, 115200);
 _port.ReadTimeout = 100;
 _port.WriteTimeout = 100;
 _port.Open(); // Serial Port Open
 _master = ModbusSerialMaster.CreateRtu(_port);
 }
 }
}
