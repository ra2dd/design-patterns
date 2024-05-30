package org.example.decorator;

import org.example.component.Notifier;

public class PushNotifierDecorator extends NotifierDecorator{
    public PushNotifierDecorator(Notifier notifier) {
        super(notifier);
    }

    @Override
    public void send(String message) {
        super.send(message);
        System.out.println("Sending Push Notification: " + message);
    }
}
