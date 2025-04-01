using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UIAct : MonoBehaviour
{
    public GameObject stop1; 
    public GameObject stop2; 
    public GameObject stop3;
    public GameObject win;
    
    public void Stop1() // Активация UI
    {
        stop1.SetActive(true);
    }
    public void Stop2() // Активация UI
    {
        stop2.SetActive(true);
    }
    public void Stop3() // Активация UI
    {
        stop3.SetActive(true);
    }
    public void Win() // Активация UI
    {
        win.SetActive(true);
    }
}
