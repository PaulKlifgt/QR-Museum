using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class ForText : MonoBehaviour
{
    // Для подстановки текста
    public Button button1;
    public Button button2;
    public Button button3;
    public Button button4;
    
    public TMP_InputField inputField1;
    public TMP_InputField inputField2;
    public TMP_InputField inputField3;
    public TMP_InputField inputField4;

    public bool autoUpdate = true; // Автоматическое обновление
    public Button applyButton;     // Кнопка применения (если autoUpdate = false)

    private void Start()
    {
        if (autoUpdate)
        {
            // Автоматическое обновление при изменении текста
            inputField1.onValueChanged.AddListener((text) => UpdateButtonText(button1, text));
            inputField2.onValueChanged.AddListener((text) => UpdateButtonText(button2, text));
            inputField3.onValueChanged.AddListener((text) => UpdateButtonText(button3, text));
            inputField4.onValueChanged.AddListener((text) => UpdateButtonText(button4, text));
            
            // Скрываем кнопку применения, если используется автообновление
            if (applyButton != null) applyButton.gameObject.SetActive(false);
        }
        else
        {
            // Ручное обновление по кнопке
            if (applyButton != null)
            {
                applyButton.onClick.AddListener(UpdateAllButtons);
                applyButton.gameObject.SetActive(true);
            }
        }
    }

    private void UpdateAllButtons()
    {
        UpdateButtonText(button1, inputField1.text);
        UpdateButtonText(button2, inputField2.text);
        UpdateButtonText(button3, inputField3.text);
        UpdateButtonText(button4, inputField4.text);
    }

    private void UpdateButtonText(Button button, string text)
    {
        TextMeshProUGUI buttonText = button.GetComponentInChildren<TextMeshProUGUI>();
        if (buttonText != null)
        {
            buttonText.text = text;
        }
        else
        {
            Debug.LogWarning($"На кнопке {button.name} не найден Text компонент!");
        }
    }

    private void OnDestroy()
    {
        // Отписываемся от всех событий
        inputField1.onValueChanged.RemoveAllListeners();
        inputField2.onValueChanged.RemoveAllListeners();
        inputField3.onValueChanged.RemoveAllListeners();
        inputField4.onValueChanged.RemoveAllListeners();
        
        if (applyButton != null) applyButton.onClick.RemoveAllListeners();
    }
}
