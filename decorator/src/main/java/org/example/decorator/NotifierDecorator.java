package org.example.decorator;

import org.example.component.Notifier;

public abstract class NotifierDecorator implements Notifier {
    protected Notifier wrapped;

    public NotifierDecorator(Notifier notifier) {
        this.wrapped = notifier;
    }

    @Override
    public void send(String message) {
        wrapped.send(message);
    }
}
