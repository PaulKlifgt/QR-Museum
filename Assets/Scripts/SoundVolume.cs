using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class SoundVolume : MonoBehaviour
{
    [SerializeField]
    private Slider slider;
    [SerializeField]
    private TMP_Text text;
    [SerializeField]
    private TMP_Text textShadow;
    public float volume = 0.8f;
    private void Start()
    {
        if (PlayerPrefs.GetFloat("hasBeenOpened") == 0)
        {
            PlayerPrefs.SetFloat("hasBeenOpened", 1);
        }
        else
        {
            volume = PlayerPrefs.GetFloat("volume", 0.8f);
            slider.value = volume;
        }
    }
    public void SoundChange()
    {

        volume = slider.value;
        Global.volume = volume;
        PlayerPrefs.SetFloat("volume", volume);
        text.text = ((int)(volume * 100f)).ToString() + "%";
        textShadow.text = ((int)(volume * 100f)).ToString() + "%";
    }
}
