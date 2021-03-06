package com.example.quote_on_quote_app;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.SeekBar;
import android.widget.TextView;

public class StartQuestionnaire extends AppCompatActivity {
    public static int EMOTION;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_start_questionnaire);

        // Get the Intent that started this activity and extract the string
        Intent intent = getIntent();
        String message = intent.getStringExtra(MainActivity.EXTRA_MESSAGE);
    }

    /** Called when the user taps the Send button */
    public void sendMessage(View view) {
        SeekBar seekBar = (SeekBar) findViewById(R.id.seekBar);
        EMOTION = seekBar.getProgress();

        Log.i("Emotion", String.valueOf(EMOTION));

        Intent intent = new Intent(this, Page2Question.class);
        startActivity(intent);
    }
}
//public class StartQuestionnaire extends AppCompatActivity {

//}
