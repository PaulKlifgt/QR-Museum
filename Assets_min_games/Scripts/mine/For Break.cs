using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ForBreak : MonoBehaviour
{
    public GameObject hole;
    public GameObject hole1;
    public GameObject hole2;
    public GameObject a1;
    public GameObject a2;
    public GameObject a3;
    public GameObject alive;

    void Breaking()
    {
        hole.SetActive(true);
        a1.SetActive(false);
        a2.SetActive(true);
    }

    void Breaking1()
    {
        hole1.SetActive(true);
        a2.SetActive(false);
        a3.SetActive(true);
    }

    void Breaking2()
    {
        hole2.SetActive(true);
        a3.SetActive(false);
    }

    void Aleving()
    {
        alive.SetActive(true);
    }

    public GameObject death;

    void Nexts()
    {
        death.SetActive(true);
    }

}
