package com.business.strategy;

import java.util.concurrent.Future;

public interface IAsyncTask
{
    public Future<String> runAsync();
}
