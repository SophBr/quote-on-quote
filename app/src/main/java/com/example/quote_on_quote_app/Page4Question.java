package com.example.quote_on_quote_app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.SeekBar;

public class Page4Question extends AppCompatActivity {
    public static int EMOTION;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_page4_question);
    }

    /** Called when the user taps the Send button */
    public void sendMessage(View view) {
        SeekBar seekBar = (SeekBar) findViewById(R.id.seekBar4);
        EMOTION = seekBar.getProgress();

        Log.i("Emotion", String.valueOf(EMOTION));

        Intent intent = new Intent(this, Page5Question.class);
        startActivity(intent);
    }
}
