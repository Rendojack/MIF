package mybatis;

import com.mybatis.dao.AuthorMapper;
import com.mybatis.dao.StudentMapper;
import com.mybatis.model.Author;
import com.mybatis.model.Book;
import com.mybatis.model.Student;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.apache.ibatis.io.Resources;
import org.junit.AfterClass;
import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

import java.util.List;


public class TestAuthorMapper
{
    private static SqlSessionFactory sqlSessionFactory;
    private static SqlSession session;
    private static StudentMapper mapper;

    @BeforeClass
    public static void setup()
    {
        try
        {
            sqlSessionFactory = new SqlSessionFactoryBuilder().build(Resources.getResourceAsStream("MyBatisConfigJDBC.xml"));
            session = sqlSessionFactory.openSession();
            mapper = session.getMapper(StudentMapper.class);

        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }

    @AfterClass
    public static void tearDown()
    {
        sqlSessionFactory = null;
        mapper = null;
        session.close();
    }

    @Test
    public void testManyToMany()
    {
        List<Student> studentList = mapper.selectAll();
        session.commit();
        Assert.assertNotNull(studentList);

        for(Student student:studentList)
        {
            System.out.println(student.getFirstName());
        }
        /*
        List<Author> authorList = mapper.selectAll();
        session.commit();

        Assert.assertNotNull(authorList);

        for (Author author:authorList)
        {
            System.out.println("AUTHOR: " + author.getFirstname() + " " + author.getLastName());
            System.out.println("BOOK LIST: ");

            List<Book> bookList = author.getBookList();
            Assert.assertNotNull(bookList);

            for(Book book:bookList)
            {
                System.out.println("    * TITLE: " + book.getTitle());
            }
            System.out.println("");
        }
        */
    }
}
