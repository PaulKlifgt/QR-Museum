using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SoundContoller : MonoBehaviour
{
    private float localVolume;
    private AudioSource audio;

    void Start()
    {
        audio = GetComponent<AudioSource>();
        localVolume = audio.volume;
    }

    void Update()
    {
        
    }
    public void ChangeVolume()
    {
        audio.volume = localVolume * Global.volume;
    }
}
