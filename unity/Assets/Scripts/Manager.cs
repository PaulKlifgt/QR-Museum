using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Manager : MonoBehaviour
{
    [SerializeField] TabButton startTabButton;


    private void Start()
    {
        startTabButton.OnClick();
    }
}