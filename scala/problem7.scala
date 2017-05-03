import scala.math._

object Pro7 {

  def isPrime(x:Int): Boolean = {
    (2 to (sqrt(x) toInt)) filter(x % _ == 0) isEmpty
  }

  def main(args: Array[String]) = {
    var primes  = List()
    val x = for(i <- 1 to 1000000) yield {
      if(isPrime(i)) i
    }
    println((x filter(_ != {}))(10001))
  }
}
