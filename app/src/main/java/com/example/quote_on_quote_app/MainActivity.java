package com.example.quote_on_quote_app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.SeekBar;

/*
    public class MainActivity extends AppCompatActivity {
    public static final String EXTRA_MESSAGE = "com.example.quote-on-quote_app.MESSAGE";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    }
    }
    */

public class MainActivity extends AppCompatActivity {
    public static final String EXTRA_MESSAGE = "com.example.quote-on-quote_app.MESSAGE";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    /** Called when the user taps the Send button */
    public void sendMessage(View view) {
        Intent intent = new Intent(this, StartQuestionnaire.class);
        startActivity(intent);
    }
}

