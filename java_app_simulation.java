import java.io.*;
import java.net.*;

public class SocketClient
{
  Socket sock;
  String server = "18.221.53.75";
  int port = 8001;
  String filename = "/foo/bar/application1.log";
  String command = "tail -50 " + filename + "\n";
  
  public static void main(String[] args)
  {
    new SocketClient();
  }
  
  public SocketClient()
  {
    openSocket();
    
  }
  
  private void openSocket()
  {
    // open a socket and connect with a timeout limit
    try
    {
      InetAddress addr = InetAddress.getByName(server);
      SocketAddress sockaddr = new InetSocketAddress(addr, port);
      sock = new Socket();
  
      // this method will block for the defined number of milliseconds
      int timeout = 2000;
      sock.connect(sockaddr, timeout);
    } 
    catch (UnknownHostException e) 
    {
      e.printStackTrace();
    }
    catch (SocketTimeoutException e) 
    {
      e.printStackTrace();
    }
    catch (IOException e) 
    {
      e.printStackTrace();
    }
  }
}