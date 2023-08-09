using System.Net;
using System.Net.Sockets;
using System.Text;
using System;
using UnityEngine;

public class AnimationController : MonoBehaviour
{
    private Animator animator;
    private TcpListener listener;
    private TcpClient client;
    private bool istalking = false;
    private bool isWaiting = false;
    private bool isDancing = false;
    private bool isIdle = false;
    public float smileDuration; // Time in seconds
    public GameObject chair;

    private void Start()
    {
        // Get reference to the Animator component
        animator = GetComponent<Animator>();
        listener = new TcpListener(IPAddress.Parse("127.0.0.1"), 8084);
        
        listener.Start();

        // Start accepting connections asynchronously
        listener.BeginAcceptTcpClient(OnClientConnected, null);
    }

    private void Update()
    {
        
         if (istalking)
        {
           if (!isWaiting)
            {
                Debug.Log("Character is talking");
                 animator.SetBool("istalking", true);
                StartCoroutine(WaitAndReset());
            }
        }
         if (isDancing)
        {
           
                Debug.Log("Character dancing");
                animator.SetBool("dance", true);
                animator.SetBool("idle", false);
                chair.SetActive(false);
           
        }
          if (isIdle)
        {
                
                Debug.Log("Character idle");
                animator.SetBool("idle", true);
                animator.SetBool("dance", false);
                chair.SetActive(true);
           
        }
        //Check for input to trigger the animation
        if (Input.GetKeyDown(KeyCode.C))
        {
            // Set the trigger parameter to start the animation
           animator.SetBool("istalking", true);
        }
        if (Input.GetKeyDown(KeyCode.D))
        {
            // Set the trigger parameter to start the animation
           animator.SetBool("istalking", false);
        }
        

        // // Check for input to toggle the bool parameter
        // if (Input.GetKeyDown(KeyCode.Space))
        // {
        //     // Invert the current value of the bool parameter
        //     animator.SetTrigger("blink");
        // }
    }
    private System.Collections.IEnumerator WaitAndReset()
    {
        isWaiting = true;
        yield return new WaitForSeconds(smileDuration);
        istalking = false;
        isWaiting = false;
        Debug.Log(smileDuration);
        animator.SetBool("istalking", false); 
    }
     void OnClientConnected(IAsyncResult ar)
    {
        client = listener.EndAcceptTcpClient(ar);

        // Start reading data from the client asynchronously
        byte[] buffer = new byte[1024];
        client.GetStream().BeginRead(buffer, 0, buffer.Length, OnDataReceived, buffer);
    }
  void OnDataReceived(IAsyncResult ar)
{
    int bytesRead = client.GetStream().EndRead(ar);
    byte[] buffer = (byte[])ar.AsyncState;

    if (bytesRead > 0)
    {
        // Convert the received data to a string
        string receivedData = Encoding.ASCII.GetString(buffer, 0, bytesRead);
        Debug.Log("receivedData: " + receivedData);

        // Split the received data into string and decimal parts
        string[] dataParts = receivedData.Split(',');

        if (dataParts.Length == 2)
        {
            // Parse the string and decimal values
            string stringValue = dataParts[0];
            float decimalValue;
            if (float.TryParse(dataParts[1], out decimalValue))
            {
                // Check the received command
                if (stringValue == "talking")
                {
                    istalking = true;
                }
                else if (stringValue == "blink")
                {
                    animator.SetTrigger("blink");
                    Debug.Log("Blinking");
                }
                else if (stringValue == "dance")
                {
                    isDancing = true;
                    isIdle = false;
                    Debug.Log("Dancing");
                }
                else if (stringValue == "stopdance")
                {
                    Debug.Log("Stop Dancing");
                    isIdle = true;
                    isDancing = false;
                }

                // Use the decimalValue as needed
                smileDuration = decimalValue;
                // ...

                // Continue reading data from the client asynchronously
                client.GetStream().BeginRead(buffer, 0, buffer.Length, OnDataReceived, buffer);
                return;
            }
        }

        // Invalid data received, handle the error
        Debug.Log("Invalid data received");

        // Continue reading data from the client asynchronously
        client.GetStream().BeginRead(buffer, 0, buffer.Length, OnDataReceived, buffer);
    }
        else
        {
            // Client has disconnected, close the connection
            client.Close();

            // Start accepting new connections asynchronously
            listener.BeginAcceptTcpClient(OnClientConnected, null);
        }
    }
     void OnApplicationQuit()
    {
        if (client != null)
        {
            client.Close();
        }

        if (listener != null)
        {
            listener.Stop();
        }
    }
}
