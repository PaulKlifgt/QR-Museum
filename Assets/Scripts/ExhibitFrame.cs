using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class ExhibitFrame : MonoBehaviour
{
    [SerializeField]
    private Image image;
    [SerializeField]
    private TMP_Text exhibitName;
    [SerializeField]
    private TMP_Text[] stars;
    [SerializeField]
    private string starSymbol;
    [SerializeField]
    private GameObject collectedImage;

    public void SetData(Sprite sprite, string stringName, float floatStars, bool isScanned)
    {
        if (isScanned)
        {
            collectedImage.SetActive(true);
        }
        exhibitName.text = stringName;
        foreach (TMP_Text star in stars)
        {
            star.text = floatStars.ToString() + starSymbol;
        }
    }
}
