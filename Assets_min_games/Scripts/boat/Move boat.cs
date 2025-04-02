using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Moveboat : MonoBehaviour
{
    public GameObject deathMenu;
    
    public void DeathMenu() // Экран поражения
    {
        deathMenu.SetActive(true);
    }
}