using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Manager : MonoBehaviour
{
    [SerializeField] TabButton startTabButton;
    [SerializeField] RectTransform cameraView;



    private void Start()
    {
        startTabButton.OnClick();
        int screenHeight = Screen.height;
        cameraView.sizeDelta = new Vector2(screenHeight, screenHeight);
        Application.targetFrameRate = 120;
    }
}