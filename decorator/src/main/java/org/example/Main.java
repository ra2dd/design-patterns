package org.example;

import org.example.component.EmailNotifier;
import org.example.decorator.PushNotifierDecorator;
import org.example.decorator.SMSNotifierDecorator;

public class Main {
    public static void main(String[] args) {
        EmailNotifier emailNotifier = new EmailNotifier();

        // emailNotifier.send("Concrete class created");
        // Output
        // Sending Email: Concrete class created

        SMSNotifierDecorator smsNotifierDecorator = new SMSNotifierDecorator(emailNotifier);
        // smsNotifierDecorator.send("Important Announcement");
        // Output
        // Sending Email: Important Announcement
        // Sending SMS: Important Announcement

        PushNotifierDecorator pushNotifierDecorator = new PushNotifierDecorator(smsNotifierDecorator);
        pushNotifierDecorator.send("New message from ...");
    }
}