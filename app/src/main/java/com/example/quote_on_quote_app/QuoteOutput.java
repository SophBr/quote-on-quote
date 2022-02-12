package com.example.quote_on_quote_app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.SeekBar;
import android.widget.TextView;

public class QuoteOutput extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_quote_output);

        int emotion_1 = StartQuestionnaire.EMOTION;
        int emotion_2 = Page2Question.EMOTION;
        int emotion_3 = Page3Question.EMOTION;
        int emotion_4 = Page4Question.EMOTION;
        int emotion_5 = Page5Question.EMOTION;
        int emotion_6 = Page6Question.EMOTION;
        int emotion_7 = Page7Question.EMOTION;
        int emotion_8 = Page8Question.EMOTION;


        String label = String.format("Emotion 1: %d \n Emotion 2: %d" , emotion_1, emotion_2);

        TextView textView = (TextView) findViewById(R.id.textView9);
        textView.setText(label);
    }

}
