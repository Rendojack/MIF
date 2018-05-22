package com.mybatis.model;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class Student
{

  private Integer id;
  private String firstName;
  private String lastName;

  @Override
  public boolean equals(Object other)
  {
    return (other != null && getClass() == other.getClass() && id != null)
            ? id.equals(((Student) other).id)
            : (other == this);
  }

  @Override
  public int hashCode()
  {
    return (id != null)
            ? (getClass().hashCode() + id.hashCode())
            : super.hashCode();
  }
  @Override
  public String toString()
  {
    return String.format("Student[%d, %s, %s]", id, firstName, lastName);
  }
}
