using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;
using TMPro;

public class ButtonShuffler : MonoBehaviour
{
    [SerializeField] private Button button1;
    [SerializeField] private Button button2;
    [SerializeField] private Button button3;

    private List<Button> buttons = new List<Button>();
    private List<Vector3> originalPositions = new List<Vector3>();

    private void Awake()
    {
        // Проверяем, что все кнопки назначены
        if (button1 == null || button2 == null || button3 == null)
        {
            Debug.LogError("Не все кнопки назначены в инспекторе!");
            return;
        }

        // Добавляем кнопки в список
        buttons.Add(button1);
        buttons.Add(button2);
        buttons.Add(button3);

        // Сохраняем оригинальные позиции
        foreach (var button in buttons)
        {
            originalPositions.Add(button.transform.position);
        }
        ShuffleButtons();
    }

    public void ShuffleButtons()
    {
        if (buttons.Count != 3 || originalPositions.Count != 3) return;

        // Создаем список индексов для перемешивания
        List<int> indexes = new List<int> { 0, 1, 2 };
        
        // Перемешиваем индексы
        for (int i = 0; i < indexes.Count; i++)
        {
            int temp = indexes[i];
            int randomIndex = Random.Range(i, indexes.Count);
            indexes[i] = indexes[randomIndex];
            indexes[randomIndex] = temp;
        }

        // Применяем новые позиции к кнопкам
        for (int i = 0; i < buttons.Count; i++)
        {
            buttons[i].transform.position = originalPositions[indexes[i]];
        }
    }
}