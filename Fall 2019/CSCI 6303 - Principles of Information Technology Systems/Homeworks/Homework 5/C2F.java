
import javax.swing.JOptionPane;
 
class C2F{
  public static void main(String[] args) {
    //Declaration
	float temperature;
	
	//Input
     
    String CelsiusString = JOptionPane.showInputDialog("Enter temperature in Celsius:");
    float Celsius = Float.parseFloat(CelsiusString) ;

	//Process 
    float Fahrenheit = (Celsius*9.0f/5) + 32;

	//Output
    JOptionPane.showMessageDialog(null, String.format("Temperature in Fahrenheit = %.2f", Fahrenheit));
    
  }
}